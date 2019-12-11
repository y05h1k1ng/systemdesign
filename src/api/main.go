package main

import (
	"github.com/ant0ine/go-json-rest/rest"
	"log"
	"math/rand"
	"net/http"
)

type position struct {
	City string
}

type typhoon struct {
	Temp   float64
	Amount float64
	Wind   float64
}

type rain struct {
	Temp   float64
	Amount float64
	Wind   float64
}

type earthquake struct {
	Temp   float64
	Amount float64
	Wind   float64
}

func rainApi(w rest.ResponseWriter, req *rest.Request) {
	input := position{}

	err := req.DecodeJsonPayload(&input)

	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	if input.City == "" {
		rest.Error(w, "City name is required", 400)
	}

	log.Printf("%#v", input)

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

func typhoonApi(w rest.ResponseWriter, req *rest.Request) {
	input := position{}

	err := req.DecodeJsonPayload(&input)

	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	if input.City == "" {
		rest.Error(w, "City name is required", 400)
	}

	log.Printf("%#v", input)

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
	input := position{}

	err := req.DecodeJsonPayload(&input)

	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	if input.City == "" {
		rest.Error(w, "City name is required", 400)
	}

	log.Printf("%#v", input)

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

func main() {
    log.Printf("[+] Server is starting...")
	api := rest.NewApi()
	api.Use(rest.DefaultDevStack...)
    
	router, err := rest.MakeRouter(
		rest.Post("/typhoon", typhoonApi),
        rest.Post("/rain", rainApi),
        rest.Post("/earthquake", earthquakeApi),
	)
	if err != nil {
		log.Fatal(err)
	}

	api.SetApp(router)
    log.Printf("[+] Server is started!")
	log.Fatal(http.ListenAndServe(":9999", api.MakeHandler()))
}
