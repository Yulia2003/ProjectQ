# ProjectQ
ProjectQ
Чтобы запустить проект нужно:
1. прописать в терминале: 
git clone https://github.com/Yulia2003/ProjectQ.git
2. установить виртуальное окрудение с помощью этой команды: 
pipenv shell
3. запустить докер:
sudo docker-compose -f docker-compose.dev.yaml up
4. сделать экспорт:
export PQ_DATABASE_URL="postgresql://root:root@localhost:32700/employment_exchange"
5. запустить fastAPI: uvicorn main:app --reload
