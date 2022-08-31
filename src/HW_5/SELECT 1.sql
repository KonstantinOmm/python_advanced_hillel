SELECT TrackId, SUM(UnitPrice), COUNT(TrackId)
FROM invoice_items
GROUP BY TrackId;