while read p; do
  echo "hadoop distcp s3://nyc-tlc/trip\ data/$p /user/hadoop/nycdata/"
done
