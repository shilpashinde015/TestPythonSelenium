import configparser

con = configparser.ConfigParser()
con.read("/home/shilpa/Git/TestPythonSelenium/configFiles/config.ini")


class Readpropertyfile:
    def getURL():
        url = con.get("Information", 'baseURL')
       # print("readproprty url : " + url)
        return url

    @staticmethod
    def getUsername():
        uName = con.get("Information", 'username')
        return uName

    @staticmethod
    def getPassword():
        passwd = con.get("Information", 'password')
        return passwd
