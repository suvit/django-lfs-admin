django-lfs-admin examle
========================

Run on heroku
    heroku create
    git push heroku master
    heroku ps:scale web=1
    heroku run python syncdb --no-input
    heroku run python loaddata lfs_user
    heroku run python loaddata lfs_shop


