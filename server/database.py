from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import bcrypt 
from datetime import datetime

class Database:
    def __init__(self, app):
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = 'admin'
        app.config['MYSQL_DB'] = 'cs6131proj'
        self.app = app
        self.mysql = MySQL(app)
    
    
    def user(self, userID):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE userID = %s', [userID])
        user = cursor.fetchone()
        cursor.execute('SELECT name, count(*) count FROM Winner w, Awards a WHERE userID = %s and w.awardID = a.awardID group by name', [userID])
        achievements = cursor.fetchall()
        cursor.close()

        return {'user': user,"achievements": achievements}
        
    def signup(
        self, email, password, username
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', [email])
        existing = cursor.fetchone()
        if existing:
            cursor.close()
            result = bcrypt.checkpw(password.encode('utf-8'), existing['hash'].encode('ascii'))
            if(result):
                return {
                    "result": True, "user": existing,
                    "message": "Account already exists, successfully logged in with details provided."
                }
            return {
                "result": False, "user": None,
                "message": "Account already exists!"
            }
        try:
            salt = bcrypt.gensalt()
            hashpw = bcrypt.hashpw(password.encode('utf-8'), salt)
            cursor.execute("INSERT INTO User (username, email, hash, salt) VALUES (%s, %s, %s, %s)", [username, email, hashpw, salt])
            self.mysql.connection.commit()
            cursor.execute('SELECT * FROM user WHERE email = %s', [email])
            existing = cursor.fetchone()
            cursor.close()
            return {
                "result": True, "user": existing, 
                "message": "Registered Successfully!"
            }
        except Exception as e:
            print(e)
            return {
                "result": False, "user": None,
                "message": str(e)
            }
        

    def login(self, email, password):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', [email])
        user = cursor.fetchone()
        cursor.close()
        if (user):
            result = bcrypt.checkpw(password.encode('utf-8'), user['hash'].encode('ascii'))
            if (result):
                return {
                'result': True, "user": user,
                "message": "Successfully logged in!"
                }
            else:
                return {
                'result': False, "user": None,
                "message": "Incorrect Password"
                }
        else:
            return {
            'result': False, "user": None,
            "message": "Account does not exist!"
            }
        

    def co2usage(
        self, userID, date
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM (SELECT * FROM Items i where userID = %s and date = %s) i RIGHT JOIN CO2Category c ON i.categoryID = c.categoryID', [userID, date])
        items = cursor.fetchall()

        if (date == datetime.today().strftime('%Y-%m-%d')):
            cursor.close()
            used = 0
            for i in items:
                if i['dol'] == None:
                    i['dol'] = 0
                used += i['CO2pDOL'] * i['dol']/1000
            return {
                "editable": True, "items": items, 'limit': 0,
                "used": used
            }
        else:
    # Code this based on date time
            cursor.execute('SELECT * FROM CO2Footprint WHERE userID = %s and date = %s', [userID, date])
            used = cursor.fetchone()
            cursor.close()

            if not used:
                return {
                    "editable": False, "items": [], 
                    "limit": 0, "used": 0
                }
            return {
                "editable": False, "items": items, 
                "limit": used['co2Limit'], "used": used['co2Usage']
            }
        
    def co2Change(
        self, userID, date, categoryID, dol, remove
    ):

        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if (remove):
            cursor.execute('DELETE FROM Items WHERE userID = %s and date = %s and categoryID = %s', [userID, date, categoryID])
            self.mysql.connection.commit()
            cursor.close()
            return {"result": True, "message": "Successfully updated!"}                     
        else:
            cursor.execute('SELECT * FROM Items WHERE userID = %s and date = %s and categoryID = %s', [userID, date, categoryID])
            existing = cursor.fetchone()
            if existing:
                cursor.execute('UPDATE Items SET dol = %s WHERE userID = %s and date = %s and categoryID = %s', [dol, userID, date, categoryID])
                self.mysql.connection.commit()
            else:
                cursor.execute('INSERT INTO Items (userID, date, categoryID, dol) VALUES (%s, %s, %s, %s)', [userID, date, categoryID, dol])
                self.mysql.connection.commit()
            cursor.close()
            return {"result": True, "message": "Successfully updated!"}
        

    def co2usage(
        self, userID, date
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM (SELECT * FROM Items i where userID = %s and date = %s) i RIGHT JOIN CO2Category c ON i.categoryID = c.categoryID', [userID, date])
        items = cursor.fetchall()

        if (date == datetime.today().strftime('%Y-%m-%d')):
            cursor.close()
            used = 0
            for i in items:
                if i['dol'] == None:
                    i['dol'] = 0
                used += i['CO2pDOL'] * i['dol']/1000
            return {
                "editable": True, "items": items, 'limit': 0,
                "used": used
            }
        else:
    # Code this based on date time
            cursor.execute('SELECT * FROM CO2Footprint WHERE userID = %s and date = %s', [userID, date])
            used = cursor.fetchone()
            cursor.close()

            if not used:
                return {
                    "editable": False, "items": [], 
                    "limit": 0, "used": 0
                }
            return {
                "editable": False, "items": items, 
                "limit": used['co2Limit'], "used": used['co2Usage']
            }
        
    def friends(
        self, userID
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT userID, username, totalPoints from Friends f, User a where f.friendA = a.userID and f.friendB = %s union SELECT userID, username, totalPoints from Friends f, User b where f.friendB = b.userID and f.friendA = %s', [userID, userID])
        friends = cursor.fetchall()
        cursor.close()
        if not friends:
            return {
                "friends": []
            }
        else:
            return {
                "friends": friends
            }
        
        
    def usersWithFriends(
        self, userID
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from User left join (SELECT friendA friendID from Friends f where f.friendB = %s union SELECT friendB friendID from Friends f where f.friendA = %s) tmp on userID=friendID order by totalPoints DESC', [userID, userID])
        users = cursor.fetchall()
        count = 1
        for i in users:
            i['rank'] = count
            count += 1
        cursor.close()
        return {
            "users": users
        }
    

    def events(
        self, userID
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select Events.eventID, name, date, points, COUNT(userID) as numFriendsAttending from Events left join (SELECT userID, eventID from Friends f, Attend e where e.userID = f.friendA and f.friendB = %s union SELECT userID, eventID from Friends f, Attend e where e.userID = f.friendB and f.friendA = %s) tmp on Events.eventID = tmp.eventID where NOT EXISTS(select * from Attend a where a.eventID = Events.eventID and userID = %s) group by Events.eventID order by date', [userID, userID,userID])
        events = cursor.fetchall()
        cursor.close()
        return {
            "events": events
        }
    
    def activities(
        self, userID, date, treeID, start
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select *, (select count(*) from ActivityReq r where treeID=%s and r.activityID = a.activityID and NOT EXISTS(select * from Completed c where c.activityID = r.activityID and userID = %s and date>%s)) treeAct from Activities a where activityID not in (select activityID from completed where userID=%s and date = %s)', [treeID, userID, start, userID, date])
        activities = cursor.fetchall()
        cursor.close()
        return {
            "activities": activities
        }
    
    def competitions(
        self, userID
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select *, (select userImage from user where userID = c.creator) avatar, (select count(*) from participate p where userID=%s and p.competitionID = c.competitionID) participate from competitions c where private=false or (%s in (SELECT p.userID from participate p where p.competitionID = c.competitionID) and private = true)', [userID, userID])
        competitions = cursor.fetchall()
        cursor.close()
        return {
            "competitions": competitions
        }
    
    def competition(
        self, userID, competitionID
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select *, (select userImage from user where userID = c.creator) avatar, (select count(*) from participate p where userID=%s and p.competitionID = %s) participate from competitions c where competitionID = %s', [userID, competitionID, competitionID])
        competition = cursor.fetchone()
        cursor.execute('select userID, points, userimage, username, friendID, count(treeID) countTrees from (select * from (select u.userID as userID, points, userimage, username from participate p, User u where p.userID = u.userID and competitionID = %s ) tmp1 left join (SELECT friendA friendID from Friends f where f.friendB = %s union SELECT friendB friendID from Friends f where f.friendA = %s) tmp on userID=friendID order by points DESC) temp2 NATURAL LEFT JOIN (select * from completedtree ct, competitions c where ct.completionDate > c.startDate and ct.completionDate < c.endDate and c.competitionID = %s) temp group by userID', [competitionID, userID, userID, competitionID])
        participants = cursor.fetchall()
        count = 1
        for i in participants:
            i['rank'] = count
            count += 1
        cursor.close()
        return {
            "competition": competition, "participants": participants
        }

    def treesUntilNow(
        self, userID
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select treeID, name, description, 0 completionDate, treeStage state from User u, Trees t where userID = %s and growTree = treeID union select * from (select t.treeID treeID, name, description, completionDate, 10 state from CompletedTree c, Trees t where userID = %s and c.treeID = t.treeID) temp order by treeId DESC', [userID, userID])
        trees = cursor.fetchall()
        cursor.close()
        return {
            "trees": trees
        }
    
    def friendChange(self, userID, friendID, add):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if add:
            if (userID < friendID):
                cursor.execute('INSERT INTO Friends (friendA, friendB) VALUES (%s, %s)', [userID, friendID])
            else:
                cursor.execute('INSERT INTO Friends (friendA, friendB) VALUES (%s, %s)', [friendID, userID])

        else:
            cursor.execute('DELETE FROM Friends WHERE (friendA = %s and friendB = %s) or (friendA = %s and friendB = %s)', [userID, friendID, friendID, userID])
        self.mysql.connection.commit()
        cursor.close()
        return {"result": True, "message": "Successfully updated!"}
    
    def insertActivity(self, userID, activityID):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO Completed (userID, activityID) VALUES (%s, %s)', [userID, activityID])
        self.mysql.connection.commit()
        user = Database.user(self, userID)['user']
        if (user.get('treeStage') == 10 and user.get('growTree') != 10):
            cursor.execute('UPDATE user set treeStage = 0, growTree = %s where userID = %s', [user.get('growTree') + 1,userID])
            self.mysql.connection.commit()

        cursor.close()
        return {"result": True, "message": "Successfully updated!"}
    

    def insertEvent(self, userID, eventID):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO Attend (userID, eventID) VALUES (%s, %s)', [userID, eventID])
        self.mysql.connection.commit()
        cursor.close()
        return {"result": True, "message": "Successfully updated!"}
    
    def joinCompetition(self, userID, competitionID):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO Participate (userID, competitionID, points) VALUES (%s, %s, 0)', [userID, competitionID])
        self.mysql.connection.commit()
        cursor.close()
        return {"result": True, "message": "Successfully updated!"}
    

    def awards(self):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from Awards')
        awards = cursor.fetchall()
        cursor.close()
        return {"awards": awards}
    
    def createCompetition(self, userID, name, description, private, award, friends, dates):
        print(award)
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if private:
            cursor.execute('INSERT INTO Competitions (creator, name, description, startDate, endDate) VALUES (%s, %s, %s, %s, %s)', [userID, name, description, dates[0], dates[1]])
            self.mysql.connection.commit()
            competitionID = cursor.lastrowid
            for i in friends:
                cursor.execute('INSERT INTO Participate (userID, competitionID, points) VALUES (%s, %s, 0)', [i['userID'], competitionID])
                self.mysql.connection.commit()
            cursor.execute('INSERT INTO Winner (userID, competitionID, awardID) VALUES (null, %s, %s)', [competitionID, award['awardID']])
            self.mysql.connection.commit()

        else:
            cursor.execute('INSERT INTO Competitions (creator, name, description, startDate, endDate) VALUES (%s, %s, %s, %s, %s)', [userID, name, description, dates[0], dates[1]])
            self.mysql.connection.commit()
            competitionID = cursor.lastrowid
            cursor.execute('INSERT INTO Participate (userID, competitionID, points) VALUES (%s, %s, 0)', [userID, competitionID])
            self.mysql.connection.commit()
            cursor.execute('INSERT INTO Winner (userID, competitionID, awardID) VALUES (null, %s, %s)', [competitionID, award['awardID']])
            self.mysql.connection.commit()
        cursor.execute('create event competitionEnd%s on schedule at %s do update Winner set userID = (select userID from participate p where competitionID = %s order by points limit 1) where competitionID = %s', [competitionID, dates[1], competitionID, competitionID])
        self.mysql.connection.commit()

        cursor.close()
        return {"comp":competitionID}
    
    def updateUser(self, userID, username, email, image, limit):
        if (image is None):
            cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE User SET username = %s, email = %s, co2limit=%s WHERE userID = %s', [username, email, limit, userID])
            self.mysql.connection.commit()
            cursor.execute('SELECT * FROM user WHERE userID = %s', [userID])
            user = cursor.fetchone()
            cursor.close()
        else:    
            cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE User SET username = %s, email = %s, userImage = %s, co2limit=%s WHERE userID = %s', [username, email, image, limit, userID])
            self.mysql.connection.commit()
            cursor.execute('SELECT * FROM user WHERE userID = %s', [userID])
            user = cursor.fetchone()
            cursor.close()
        return {"result": True, "message": "Successfully updated!", "user": user}
    
    def searchCompetitions(
        self, userID, query
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select *, (select userImage from user where userID = c.creator) avatar, (select count(*) from participate p where userID=%s and p.competitionID = c.competitionID) participate from competitions c where (private=false or (%s in (SELECT p.userID from participate p where p.competitionID = c.competitionID) and private = true)) and name like %s', [userID, userID, '%' + str(query) + '%'])
        competitions = cursor.fetchall()
        cursor.close()
        return {
            "competitions": competitions
        }
    
    def searchEvents(
        self, userID, query
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select Events.eventID, name, date, points, COUNT(userID) as numFriendsAttending from Events left join (SELECT userID, eventID from Friends f, Attend e where e.userID = f.friendA and f.friendB = %s union SELECT userID, eventID from Friends f, Attend e where e.userID = f.friendB and f.friendA = %s) tmp on Events.eventID = tmp.eventID where NOT EXISTS(select * from Attend a where a.eventID = Events.eventID and userID = %s) and name like %s group by Events.eventID order by date', [userID, userID,userID,  '%' + str(query) + '%'])
        events = cursor.fetchall()
        cursor.close()
        return {
            "events": events
        }

    def searchActivities(
        self, userID, date, treeID, start, query
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select *, (select count(*) from ActivityReq r where treeID=%s and r.activityID = a.activityID and NOT EXISTS(select * from Completed c where c.activityID = r.activityID and userID = %s and date>%s)) treeAct from Activities a where activityID not in (select activityID from completed where userID=%s and date = %s) and name like %s', [treeID, userID, start, userID, date, '%' + str(query) + '%'])
        activities = cursor.fetchall()
        cursor.close()
        return {
            "activities": activities
        }
    
        
    def searchFriends(
        self, userID, query
    ):
        cursor = self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from User left join (SELECT friendA friendID from Friends f where f.friendB = %s union SELECT friendB friendID from Friends f where f.friendA = %s) tmp on userID=friendID where username like %s order by totalPoints DESC', [userID, userID,'%' + str(query) + '%'])
        users = cursor.fetchall()
        count = 1
        for i in users:
            i['rank'] = count
            count += 1
        cursor.close()
        return {
            "users": users
        }
    