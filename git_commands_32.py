"""
git init -> .git (создается скрытая папка)
git remote add (origin)<name url> -> добавляет удаленный репозиторий
git pull origin master -> стягиваем изменения с ветки
git status -> показывает статус файла проекта
git add -> добавляет файлы в рабочей папке в индекс(origin)
git <name file> -> добавит только этот файл в индекс
git add . -> добавит все измененные файлы в индекс
git commit -m "comment" -> добавляет все файлы в индекс
git branch -> менеджер веток
git branch <name branch> -> создает ветку с названием
git checkout <name branch> -> проdодит на ветку с именем
git push (origin master) <name branch> -> отправляет на удаленный репозиторий
git reset <file name> -> удаляет файл из индекса


"""

# sudo apt-get install git

# Регистрация в github/gitlab/bitbucket

# настройка
# git config --global user.email "shermatovbaianas@gmail.com(почта)"
# git config --global user.name "baianas(имя)"

# создание ключа
# ssh-keygen #-t rsa -> етод шифрования

# cat ~/.ssh/id_rsa.pub показывает публичный ключ

# полученный ключ добавляем в профиль github

# создание нового репозитория

# git init - преврашаем текущую директорию в git репозиторий

# git remote add origin(название, можно любое, но предпочтительно origin) git@github.com:baianas/test_repo.git
#
# git remote -v -> посмотр списка удаленных репозиториев
# git remote rm <имя> -> удаление из списка


"""Работа с репозиторием"""
# git status - проверка изменений
# git diff - проверка изменений построчно

# git add <название файла> -> добавялет файл(ы) в версию(закомитить)

# git commit -m "Add file1" -> на основе добавленных файлов создаёт коммит(версию)

# git log - просмотр изменений

# git log --oneline - короткая версия просмотра истории версий

# git log -p

# git push origin master - пушить код из локального в удаленный

# git push -> отправка версии в удаленный репозиторий

# git clone <ссылка>

# git pull - получение версий из удаленного репзитория

# git checkout - переход по веткам
# git branch - список веток
# git branch имя - создание ветки
# git branch -D имя - удалять ветку

# git checkout -b имя - создание ветки и переход на нее
# git checkout имя_файлв - отмена изменений в файле

# git reset - удаление файлов из staging area
# git reset имя
# git reset HEAD~ - удаление коммитов


