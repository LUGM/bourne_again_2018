#!/usr/bin/env bash

while
	read -p "Username: " username
	[[ ! "$username" =~ ^[a-z0-9]{5,12}$ ]]
do
	echo "$username is not a valid username"
done

while
	read -p "Email ID: " email
	[[ ! "$email" =~ ^[a-z0-9_\.]+@[a-z0-9\-]+\.[a-z]+$ ]]
do
	echo "$email is not a valid email address"
done

while
	read -sp "Password: " password
	[[ ! "$password" =~ ^[^\s]{8,}$ ]]
do
	echo "Invalid password"
done

echo -e "$username\t$email\t$password" >> form.txt
echo
