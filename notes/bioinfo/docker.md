## detele image
```
$ docker image rm f0d8d8384898
Error response from daemon: conflict: unable to delete f0d8d8384898 (must be forced) - image is being used by stopped container 32e837b80237
```

<https://stackoverflow.com/questions/65895928/how-to-delete-a-docker-image>

```
 docker system prune
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - unused build cache
```

