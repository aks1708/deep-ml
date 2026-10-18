-- your query
SELECT min(id), email
FROM person
GROUP BY 2
ORDER BY 1 ASC
