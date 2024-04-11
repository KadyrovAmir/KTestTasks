SELECT
    root.project,
    root.id "root_id",
    (SELECT COUNT(*)
     FROM A "branch"
     WHERE branch.parent_id = root.id AND branch.type = 'branch') "branch_count",
    (SELECT COALESCE(ARRAY_AGG(DISTINCT leaf.extra->>'color'), '{}')
     FROM A "branch"
     INNER JOIN A "leaf" ON branch.id = leaf.parent_id AND leaf.type = 'leaf'
     WHERE branch.parent_id = root.id AND branch.type = 'branch' AND leaf.extra->>'color' IS NOT NULL) "leaf_colors"
FROM A "root"
WHERE root.type = 'root' AND root.project = 1;
