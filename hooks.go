package main

import (
	"fmt"

	"github.com/snikch/goodman/hooks"
	trans "github.com/snikch/goodman/transaction"
)

func main() {
	h := hooks.NewHooks()
	s := hooks.NewServer(hooks.NewHooksRunner(h))
	h.Before("/config > GET", func(t *trans.Transaction) {
		fmt.Println("before GET /config")
	})
	s.Serve()
	defer s.Listener.Close()
}
