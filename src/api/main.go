package main

import (
	"github.com/ant0ine/go-json-rest/rest"
	"log"
	"net/http"
	"math/rand"
)

type postHelloInput struct {
    City string
}

type postHelloOutput struct {
    Level int
}

func postApi(w rest.ResponseWriter, req *rest.Request) {
    input := postHelloInput{}

    err := req.DecodeJsonPayload(&input)

    if err != nil {
        rest.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    if input.City == "" {
        rest.Error(w, "City name is required", 400)
    }

    log.Printf("%#v", input)

    err = w.WriteJson(postHelloOutput{
        rand.Intn(10),
    })

    if err != nil {
        rest.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
}

func main() {
    api := rest.NewApi()
    api.Use(rest.DefaultDevStack...)
    router, err := rest.MakeRouter(
        rest.Post("/api", postApi),
    )

    if err != nil {
        log.Fatal(err)
    }
    log.Printf("[+] Server started...")
    api.SetApp(router)
    log.Fatal(http.ListenAndServe(":9999", api.MakeHandler()))
}
