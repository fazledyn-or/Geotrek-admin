-- Interventions


CREATE VIEW {{ schema_geotrek }}.v_interventions AS
SELECT a.id,
       e.name AS "Structure",
       f.zoning_city AS "City",
       g.zoning_district AS "District",
       a.name AS "Name",
       a.date AS "Date",
       d.stake AS "Stake",
       c.status AS "Status",
       b.type AS "Type",
       CASE
           WHEN a.subcontracting IS FALSE THEN 'No'
           WHEN a.subcontracting IS TRUE THEN 'Oui'
       END AS "Subcontracting",
       i.disorder AS "Disorders",
       a.material_cost AS "Material cost",
       a.heliport_cost AS "Heliport cost",
       a.subcontract_cost AS "Subcontract cost",
       j.job AS "Job",
       j.cost AS "Mandays",
       j.nb_days AS "Cost",
       (a.material_cost+a.heliport_cost+a.subcontract_cost)::float AS "Total cost",
       h.name AS "Project",
       CASE
           WHEN k.app_label = 'core' THEN 'Tronçons'
           WHEN k.app_label = 'infrastructure' THEN 'Aménagements'
       END AS "Related object",
       CONCAT(a.min_elevation, ' m') AS "Elevation minimum",
       CONCAT(a.max_elevation, ' m') AS "Elevation maximum",
       CONCAT ('h: ',height::numeric(10, 2), 'm , L: ', a.LENGTH::numeric(10, 2),'m , l: ', width::numeric(10, 2),'m : ', area::numeric(10, 1), 'm²') AS "Dimensions",
       a.description AS "Description",
       a.date_insert AS "Insertion date",
       a.date_update AS "Update date",
       a.geom_3d
FROM maintenance_intervention a
LEFT JOIN maintenance_interventiontype b ON a.type_id = b.id
LEFT JOIN maintenance_interventionstatus c ON a.status_id = c.id
LEFT JOIN core_stake d ON a.stake_id = d.id
LEFT JOIN authent_structure e ON a.structure_id = e.id
LEFT JOIN maintenance_project h ON a.project_id = h.id
LEFT JOIN
    (SELECT array_to_string(ARRAY_AGG (b.name ORDER BY b.name), ', ', '_') zoning_city,
            a.id
     FROM maintenance_intervention a
     JOIN zoning_city b ON ST_INTERSECTS (st_pointonsurface(a.geom_3d), b.geom)
     GROUP BY a.id) f ON a.id = f.id
LEFT JOIN
    (SELECT array_to_string(ARRAY_AGG (b.name ORDER BY b.name), ', ', '_') zoning_district,
            a.id
     FROM maintenance_intervention a
     JOIN zoning_district b ON ST_INTERSECTS (st_pointonsurface(a.geom_3d), b.geom)
     GROUP BY a.id) g ON a.id = g.id
LEFT JOIN
    (SELECT array_to_string(ARRAY_AGG (disorder  ORDER BY a.id), ', ', '_') disorder,
            c.id
     FROM maintenance_interventiondisorder a
     JOIN maintenance_intervention_disorders b ON a.id = b.interventiondisorder_id
     JOIN maintenance_intervention c ON b.intervention_id = c.id
     GROUP BY c.id) i ON a.id = i.id
LEFT JOIN
    (SELECT a.id,
            sum(b.nb_days)nb_days,
            max(c.job) job,
            sum(c.cost) "cost"
     FROM maintenance_intervention a
     JOIN maintenance_manday b ON a.id = b.intervention_id
     JOIN maintenance_interventionjob c ON c.id= b.job_id
     GROUP BY a.id) j ON a.id = j.id
LEFT JOIN
    (SELECT target_type_id,
            b.app_label
     FROM public.maintenance_intervention a
     JOIN django_content_type b ON a.target_type_id = b.id
     GROUP BY target_type_id,
              app_label) k ON a.target_type_id = k.target_type_id
JOIN core_topology l ON a.target_id = l.id
WHERE a.deleted = FALSE 
 ;

-- Chantiers

CREATE VIEW {{ schema_geotrek }}.v_projects AS
SELECT a.id,
       c.name AS "Structure",
       a.name AS "Name",
       coalesce(a.begin_year::varchar || ' - ' || a.end_year::varchar, a.begin_year::varchar, a.end_year::varchar) AS "Period",
       b.type AS "Type",
       e.domain AS "Domain",
       a.begin_year AS "Begin year",
       a.end_year AS "End year",
       a.global_cost AS "Global cost",
       a."constraint" AS "Constraint",
       h.organism AS "Project owner",
       j.organism AS "Project manager",
       k.contractor AS "Contractors",
       i.financement AS "Fundings",
       a.comments AS "Comments",
       a.date_insert AS "Insertion date",
       a.date_update AS "Update date"
FROM maintenance_project a
LEFT JOIN maintenance_projecttype b ON a.type_id = b.id
LEFT JOIN authent_structure c ON a.structure_id = c.id
LEFT JOIN maintenance_projectdomain e ON a.domain_id = e.id
LEFT JOIN common_organism h ON a.project_owner_id = h.id
LEFT JOIN common_organism j ON a.project_manager_id = j.id
LEFT JOIN
    (WITH financements AS
         (SELECT a.id,
                 amount,
                 project_id,
                 organism_id,
                 c.organism,
                 CASE
                     WHEN amount IS NOT NULL THEN concat(amount::numeric(10, 1), '€ de ', c.organism)
                     ELSE NULL
                 END AS financement
          FROM maintenance_funding a
          JOIN maintenance_project b ON a.project_id = b.id
          JOIN common_organism c ON a.organism_id = c.id) SELECT project_id,
                                                                 array_to_string(ARRAY_AGG (financement  ORDER BY financements.id), ', ', '_') financement
     FROM financements
     GROUP BY project_id) i ON a.id = i.project_id
LEFT JOIN
    (SELECT a.contractor,
            b.contractor_id,
            project_id
     FROM maintenance_contractor a
     JOIN maintenance_project_contractors b ON a.id = b.contractor_id
     JOIN maintenance_project c ON b.project_id = c.id) k ON a.id = k.project_id
WHERE a.deleted IS FALSE 
;
