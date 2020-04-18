## Commands
### HDFS Commands
#### Test sample of the input data before Hadoop
Create the testfile
```head -50 purchase.txt > testfile```
Test with mapper
```cat testfile | ./mapper.py | sort | ./reducer.py```
#### Running the Hadoop job - This is the shortcut command by Cloudera </br>
```hs mapper.py reducer.py inputDir outputDir```
  - It's short for: </br>
    ```bash
    $ type map_reduce

    run_mapreduce() {
      hadoop jar /usr/lib/hadoop-2.0-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper $1 -reducer $2 -file $1 -file $2 -input $3 -output $4
    }
    ```
#### See the Output Directory
```hadoop fs -ls outputDir```

#### View the output file (Ex: part-00000)
```hadoop fs -cat outputDir/part-00000 | less```

#### Add input data to HDFS
```
cd udacity_training/data
```
Add purchases.txt
```
hadoop fs -put purchases.txt
```
Check the file is present in HDFS
```
hadoop fs -ls
```

#### Other helpful commands
Deleting a directory on HDFS
```
hadoop fs -rm -r outputDir
```
