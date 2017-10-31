## mLab Setup

1. Go to [heroku](https://www.heroku.com) and navigate to your main page. 

2. Click new, `Create new app` and name your app.

  ![create app](/Images/create_app.png)

3. Locate the Resources tabs and add `mLab MongoDB` then select the free version.

  ![Resource tab](/Images/resource_tab.png)
  
  ![free](/Images/free_version.png)
  
4. Click on your created link to bring you to the mLab Page.

5. This connection string will be what is used to connected to your database. 

  ![Connection String](/Images/connection_string.png)
 
 6. Click the `Users` tabs and `add database user`. You will use this user name and password in your connection string. 
  
  ![add user](/Images/add_user.png)
  
 7. To confirm Open up a shell and enter `mongo` followed by your connection string. Then run `db.new_collection("Test":"McTestFace")`. If everything worked you are set to go!