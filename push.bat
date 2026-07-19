@echo off
echo ==========================================================
echo  Pushing Ultra-Professional GitHub Profile README to GitHub
echo ==========================================================

git init
git branch -M main
git remote remove origin 2>nul
git remote add origin https://github.com/abhikumar002/abhikumar002.git
git add .
git commit -m "feat: setup ultra-professional github profile readme and snake workflow"
git push -u origin main

echo ==========================================================
echo  Successfully Pushed to https://github.com/abhikumar002/abhikumar002
echo ==========================================================
pause
