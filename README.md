
## Harry Jiawei Hu 

This is lab assignment 3 'Docker' which builds on lab assignment 1 'Flask' . In this lab, we learn about the merits and conveniences of docker images, and try to incorporate it with our flask server that we made previously. 


# Activity 1

From the local repository of lab1 flask, a new branch was created for this lab - titled 'lab3'. 
- [x] clearned up README.md on lab 3 branch
- [x] pushed lab3 branch to github 
- [x] set the new branch as default branch 


# Activity 2 

![installation](screenshot_assets/lab3/lab3activity1.JPG)

Screenshot of 'Docker Version' in windows command terminal - showing the successful installation of Docker

# Activity 3

![locally_hellodocker](screenshot_assets/lab3/lab3activity3.JPG)

Screenshot of the application running locally after changing title to "Hello [your name]! Welcome to Lab3 Docker!". This is to ensure the code base works well before dokerizing it. 

# Activity 4

![docker_build_psa_](screenshot_assets/lab3activity4p1.JPG)

- Built and ran docker images with the docker commands above 
- Reinstalled python dependencies in Docker through Dockerfile and copying from requirements.txt

![docker_ps-a_outcome](screenshot_assets/lab3activity4p2.JPG)

Screenshot showing container successfully running. The log information indicates the running application after the 'docker ps -a' command.

![app_running_localhost](screenshot_assets/lab3screenshotp5.JPG)

Screenshot showing application running on http://localhost:5000 at the time that it was taken. 