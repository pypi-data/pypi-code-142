from datetime import datetime

#Author: Muhammad Osama Khan
class ViewRecord:

    #Creating Table if not Exist to save Viewers Record
    def createTableIfNotExist(self, conn):
        cursor=conn.cursor()
        create_table="""
        Create Table IF NOT EXISTS ViewRecord(my_user varchar(100), target_user varchar(100), viewedAt varchar(100))
        """
        cursor.execute(create_table)

    #Creating table ViewRecord if not created and Inserting my user and other user of which profile is being viewed.
    def insert_view_record(self, conn, my_user, target_user):
        if my_user != target_user:
            self.createTableIfNotExist(conn)
            
            cursor = conn.cursor()
            viewedAt = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("INSERT INTO ViewRecord (my_user, target_user, viewedAt) VALUES (%s,%s,%s)",(my_user, target_user, viewedAt))
            conn.commit()
            return 'View Added'
        return 'Self view entry not allowed'
        
    #Returning number of viewers of your profile
    def get_your_profile_view_record(self, conn, my_user):
        cursor=conn.cursor()
        cursor.execute("SELECT count(*) FROM ViewRecord where target_user='" + my_user + "'")
        details = cursor.fetchall()
        print(details)
        return details
        
        
    #Returning number of viewers of your profile
    def top_profiles(self, conn, limit):
        cursor=conn.cursor()
        cursor.execute("SELECT target_user, count(*) as totalViewers FROM ViewRecord Group By target_user Order By Count(*) Desc")
        details = cursor.fetchall()
        print(details)
        return details
        
    

