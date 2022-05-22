import mysql.connector

class DBMySQL():
    def __init__(self):
        self.conector = mysql.connector.connect(user='root', password='', host='localhost',port=3306, database='world',auth_plugin='mysql_native_password')
    
    def getAllCountrys(self):
        cursor = self.conector.cursor()
        sql = "SELECT * from country"
        cursor.execute(sql)
        data = []
        for (Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2 ) in cursor.fetchall():
            data.append({'Code':Code, 'Name':Name, 'Continent':Continent, 'Region':Region, 'SurfaceArea':SurfaceArea, 'IndepYear':IndepYear, 'Population':Population, 'LifeExpectancy':LifeExpectancy, 'GNP':GNP, 'GNPOld':GNPOld, 'LocalName':LocalName, 'GovernmentForm':GovernmentForm, 'HeadOfState':HeadOfState, 'Capital':Capital, 'Code2':Code2})
        return data

    def findByCodeCountry(self, code):
        cursor = self.conector.cursor()
        sql = "SELECT * from country WHERE Code like '%" + code + "%'"
        cursor.execute(sql)
        data = []
        for (Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2 ) in cursor.fetchall():
            data.append({'Code':Code, 'Name':Name, 'Continent':Continent, 'Region':Region, 'SurfaceArea':SurfaceArea, 'IndepYear':IndepYear, 'Population':Population, 'LifeExpectancy':LifeExpectancy, 'GNP':GNP, 'GNPOld':GNPOld, 'LocalName':LocalName, 'GovernmentForm':GovernmentForm, 'HeadOfState':HeadOfState, 'Capital':Capital, 'Code2':Code2})
        return data
    
    def actualizarCountry(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o ):
        cursor = self.conector.cursor()
        sql = "UPDATE country SET Name = %s, Continent = %s, Region = %s, SurFaceArea = %s, IndepYear = %s, Population = %s, LifeExpectancy = %s, GNP = %s, GNPOld = %s, LocalName = %s, GovernmentForm = %s, HeadOfState = %s, Capital = %s, Code2 = %s WHERE Code = %s"
        val = (b, c, d, e, f, g, h, i, j, k, l, m, n, o, a)
        cursor.execute(sql, val)
        data = []
        for (Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2 ) in cursor.fetchall():
            data.append({'Code':Code, 'Name':Name, 'Continent':Continent, 'Region':Region, 'SurfaceArea':SurfaceArea, 'IndepYear':IndepYear, 'Population':Population, 'LifeExpectancy':LifeExpectancy, 'GNP':GNP, 'GNPOld':GNPOld, 'LocalName':LocalName, 'GovernmentForm':GovernmentForm, 'HeadOfState':HeadOfState, 'Capital':Capital, 'Code2':Code2})
        self.conector.commit()
        return data
    
    def insertarCountry(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o ):
        cursor = self.conector.cursor()
        sql = "INSERT INTO country (Code, Name, Continent, Region, SurFaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2  ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o)
        cursor.execute(sql, val)
        self.conector.commit()
        
    def eliminarByCodeCountry(self, code):
        cursor = self.conector.cursor()
        sql = "DELETE FROM country WHERE Code like '%" + code + "%'"
        cursor.execute(sql)
        self.conector.commit()
        
    def closeConnection(self):
        self.conector.close()