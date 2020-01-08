package main

import (
	"github.com/ant0ine/go-json-rest/rest"
	"log"
	"math/rand"
	"net/http"
)

type tsunami struct {
	Type   string
    Level  int
}

type rain struct {
    Type   string
    Level  int
}

type earthquake struct {
    Type string
    Level int
}

type volcano struct {
    Type string
    Level int
}

func rainApi(w rest.ResponseWriter, req *rest.Request) {
	err = w.WriteJson(rain{
		rand.Float64(),
		rand.Float64(),
		rand.Float64(),
	})

	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}

func tsunamiApi(w rest.ResponseWriter, req *rest.Request) {
	err = w.WriteJson(typhoon{
		rand.Float64(),
		rand.Float64(),
		rand.Float64(),
	})

	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}

func earthquakeApi(w rest.ResponseWriter, req *rest.Request) {
	err = w.WriteJson(earthquake{
		rand.Float64(),
		rand.Float64(),
		rand.Float64(),
	})

	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}
func volcanoApi(w rest.ResponseWriter, req *rest.Request) {
	err = w.WriteJson(rain{
		rand.Float64(),
		rand.Float64(),
		rand.Float64(),
	})

	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}

func main() {
    log.Printf("[+] Server is starting...")
	api := rest.NewApi()
	api.Use(rest.DefaultDevStack...)
    
	router, err := rest.MakeRouter(
		rest.Get("/tsunami", tsunamiApi),
        rest.Get("/rain", rainApi),
        rest.Get("/earthquake", earthquakeApi),
        rest.Get("/volcano", volcanoApi),
	)
	if err != nil {
		log.Fatal(err)
	}

	api.SetApp(router)
    log.Printf("[+] Server is started!")
	log.Fatal(http.ListenAndServe(":9999", api.MakeHandler()))
}
