CREATE PROCEDURE GetUser
    @UserId VARCHAR(50)
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX);

    SET @sql =
        'SELECT *
         FROM Users
         WHERE Id = ' + @UserId;

    EXEC(@sql);
END;