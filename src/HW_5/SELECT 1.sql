SELECT TrackId, SUM(UnitPrice), SUM(Quantity)
FROM invoice_items
GROUP BY TrackId;