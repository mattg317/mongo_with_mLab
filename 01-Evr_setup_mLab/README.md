## mLab Setup

1. Go to [heroku](https://www.heroku.com) and navigate to your main page. 

2. Click `New` then click `Create new app`. 

  ![create app](/Images/create_app.png)

3. On the next screen make sure to name your app then click `Create App`.

4. Locate the Resources tabs and add `mLab MongoDB` .

  ![mlab](/Images/mLab_addon.png)

5. Select the free version.
  
  ![free](/Images/free_version.png)
  
6. Click on your created link to bring you to the mLab Page.

7. The connection string at the top of the page will be used to connect to your database. 

  ![Connection String](/Images/connection_string.png)
 
8. Add a new user by clicking the `Users` tab and `Add database user`. Create a username and password. You will use these in your connection string to replace `<dbuser>` and `<dbpassword>`. 
  
  ![add user](/Images/add_user.png)
  
9. To confirm, open up a shell and enter `mongo` followed by your connection string. 

  ![mongo shell](/Images/mongo_shell.png)

10. Run `db.test_collection.insert({"Test":"McTestFace"})` in mongo shell. If everything worked you are set to go!

  ![document insert](/Images/doc_insert.png)