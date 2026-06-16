CREATE PROCEDURE GetError
AS
BEGIN
    BEGIN TRY
        SELECT * FROM SecretTable;
    END TRY
    BEGIN CATCH
        SELECT ERROR_MESSAGE(),
               ERROR_PROCEDURE(),
               ERROR_LINE();
    END CATCH
END;