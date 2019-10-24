SELECT FirstName, LastName, City, State
FROM Person as p
LEFT JOIN Address as a
ON p.PersonId = a.PersonId