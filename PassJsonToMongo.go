// It inserts large json file to mongodb

package main 

import (
    "bufio"
    "os"
    "log"
    "encoding/json"
    "strings"
    "gopkg.in/mgo.v2"
    "io"
)


func TrimSuffix(s, suffix string) string {
    if strings.HasSuffix(s, suffix) {
        s = s[:len(s)-len(suffix)]
    }
    return s
}


func main(){

    // Create connection 
    session, err := mgo.Dial("mongodb://localhost:27017")

    if err != nil {
            panic(err)
    }
    defer session.Close()

    collection := session.DB("db_name").C("collection")

    // read file 
    file, err := os.Open("track-part2-1551268151082.json")
    if err != nil{
        log.Fatal(err)
    }
    defer file.Close()

    reader := bufio.NewReader(file)

    for {
        text, err := reader.ReadString('\n')
        if err == io.EOF {
            break
        }
        s := TrimSuffix(text, ",\n")
        var result map[string]interface{}
        err = json.Unmarshal([]byte(s), &result)
        if err != nil{
            log.Fatal(err)
        }
        err = collection.Insert(result)
        if err != nil {
            log.Fatal(err)
        }
    }
}
