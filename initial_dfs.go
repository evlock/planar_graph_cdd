package main

import (
	"fmt"
)

type DEQueue struct {
	front *Cell
	back *Cell
}

type Cell struct {
	value int
	next *Cell
	prev *Cell
}

func NewDEQueue() *DEQueue {
	return &DEQueue{nil, nil}
}

func (dq *DEQueue) IsEmpty() bool {
	if dq.front == nil {
		return true
	}
	return false
}

func (dq *DEQueue) EnqueueFront(v int) {
	newCell := &Cell{v, dq.front, nil}
	if dq.IsEmpty() == true {			// if theres nothing, back == front
		dq.back = newCell
	} else {
		dq.front.prev = newCell
	}
	dq.front = newCell
}

func (dq *DEQueue) EnqueueBack(v int) {
	newCell := &Cell{v, nil, dq.back}
	if dq.IsEmpty() == true {
		dq.front = newCell
	} else {
		dq.back.next = newCell
	}
	dq.back = newCell
}

func (dq *DEQueue) DequeueFront() int {
	front := dq.front.value
	if dq.front == dq.back {		// if theres 1 thing in the list
		dq.back = nil
		dq.front = nil
	} else {
		dq.front = dq.front.next
	}
return front
}

func (dq *DEQueue) DequeueBack() int {
	back := dq.back.value
	if dq.front == dq.back {
		dq.back = nil
		dq.front = nil
	} else {
		dq.back = dq.back.prev
	}
	return back
}



type Graph struct {
	vertices int
	edges []*Edges
}

type Edges struct {
	target int
	next *Edges
}

func NewGraph(n int) *Graph {
	edge := make([]*Edges, n)
	return &Graph{n, edge}
}

func (g *Graph) Print(names []string) {
	if g == nil {
		return
	}
	for i := range g.edges {
		fmt.Println(names[i])
		for curr := g.edges[i]; curr != nil; curr = curr.next {
			fmt.Printf("   %s\n", names[curr.target])
		}
	}
}

func (g *Graph) AddEdge(source int, target int) {
	newEdge := &Edges{target, nil}			// making new edge pointing to nothing 

	curr := g.edges[source]					// iterating thru a source's linked list to insert new edge 

	if curr == nil {
		g.edges[source] = newEdge
		return
	}

	g.HelpEdge(curr, newEdge, target)
}

func (g *Graph) HelpEdge(curr *Edges, e *Edges, target int) {
	if curr.target == e.target {						// so u dont add same thing twice 
		return
	}
	if curr.next != nil && curr.next.target == target {	// checking if 
		return
	}
	if curr.next != nil && curr.next.target > target {
		e.next = curr.next
		curr.next = e
		return
	}
	if curr.next == nil {
		curr.next = e
		return
	}
	g.HelpEdge(curr.next, e, target)
}

func DFS(g *Graph, start int, names []string) {
	q := NewDEQueue()
	dist := NewDEQueue()
	color := make([]int, g.vertices)			// array of size graph 

	color[start] = 1 							// color = red 

	q.EnqueueFront(start)
	dist.EnqueueFront(0)

	for q.IsEmpty() == false {					// as long as the queue isnt empty
		v := q.DequeueFront()
		if color[v] != 2 {
			color[v] = 2

			fmt.Printf("Visiting %s\n", names[v])

			vertex := g.edges[v]
			for vertex != nil {						// add vertex's links to queue
				if color[vertex.target] != 2 {
					color[vertex.target] = 1		// red
					q.EnqueueFront(vertex.target)	// enqueue 
				} 

				vertex = vertex.next
			}
		}							// green
	
		
		
	}
}

func makeCities() (*Graph, []string) {
	cities := []string {"Montreal", "Boston", "New York City", "Philadelphia", "Pittsburgh", "Atlanta", "Miami", "New Orleans", "Chicago", "Minneapolis", "Tulsa", "Denver", "Houston", "Austin", "Los Angeles", "San Francisco", "Seattle", "Vancouver"}


	mappy := NewGraph(18)			// establishing the graph 

	map_edges := [][]int {
		{1},							// 0: Montreal
		{0, 2, 6}, 						// 1: Boston
		{1, 3}, 						// 2: New York City
		{2, 4, 5, 7, 11}, 				// 3: Philadelphia
		{3, 8}, 						// 4: Pittsburgh
		{3}, 							// 5: Atlanta
		{1}, 							// 6: Miami
		{3}, 							// 7: New Orleans
		{4, 11}, 						// 8: Chicago
		{11}, 							// 9: Minneapolis
		{14}, 							// 10: Tulsa
		{3, 8, 9, 14}, 					// 11: Denver
		{13, 14}, 						// 12: Houston
		{12}, 							// 13: Austin
		{10, 11, 12, 15, 16}, 			// 14: Los Angeles
		{14},							// 15: San Francisco
		{14, 17}, 						// 16: Seattle
		{16},							// 17: Vancouver
	}

	for i := 0; i < len(map_edges); i++ {
		for j := 0; j < len(map_edges[i]); j++ {
			mappy.AddEdge(i, map_edges[i][j])
		}
	}

	return mappy, cities
}

func PrintQueue(dq *DEQueue) {
    if dq == nil {
        return
    }
    curr := dq.front
    fmt.Printf("-> ")
    for curr != nil {
        fmt.Printf("%d ", curr.value)
        curr = curr.next
    }
    fmt.Println("->")
}

func main() {
	g, names := makeCities()
	// fmt.Println("--------------------------------------------------")
	// g.Print(names)
	// fmt.Println("--------------------------------------------------")
	fmt.Println("Breadth-first search starting from Montreal")
	BFS(g, 0, names)
	fmt.Println("--------------------------------------------------")
	fmt.Println("Breadth-first search starting from Chicago")
	BFS(g, 8, names)
	fmt.Println("--------------------------------------------------")
	fmt.Println("Breadth-first search starting from Austin")
	BFS(g, 13, names)
	fmt.Println("--------------------------------------------------")
	fmt.Println("Depth-first search starting from Montreal")
	DFS(g, 0, names)
	fmt.Println("--------------------------------------------------")
	fmt.Println("Depth-first search starting from Chicago")
	DFS(g, 8, names)
	fmt.Println("--------------------------------------------------")
	fmt.Println("Depth-first search starting from Austin")
	DFS(g, 13, names)
}

