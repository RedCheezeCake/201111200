%%writefile src/ds_rest_subway_mongo.js
use ds_rest_subwayPassengers_mongo_db
db.db_rest_subway.find({"CardSubwayStatisticsService.row.SUB_STA_NM":"강남구청"})
