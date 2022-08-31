SELECT albums.Title AS 'Album Name',
		genres.Name AS 'Genre',
		tracks.Composer AS 'Artists or Group',
		SUM(tracks.Milliseconds)/60000 AS 'Duration (Minuts)',
		SUM(tracks.Bytes)/1048576 AS 'Size (Mb)',
		COUNT(tracks.TrackId) AS 'Count tracks',
		media_types.Name AS 'Media Type'
FROM tracks
INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
INNER JOIN genres ON tracks.GenreId = genres.GenreId
INNER JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
WHERE media_types.Name = 'MPEG audio file' AND tracks.Composer IS NOT NULL
GROUP BY albums.Title
ORDER BY genres.Name, tracks.Composer;
