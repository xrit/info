#
# README file 
# Apache Docker 
# 

# To build apache on docker 
docker build -t apachedocker .

# To run apache on docker 
docker run -p 81:80 -d apachedocker

# To check images
docker images

# To check running container
docker ps

# To ping running container on newly built instance/image locally
curl -i localhost:81

