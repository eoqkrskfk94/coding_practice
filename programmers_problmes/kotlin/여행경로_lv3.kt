class Solution {
    var possibleRoutes = mutableListOf<List<String>>()

    fun solution(tickets: Array<Array<String>>): Array<String> {
        var answer = arrayOf<String>()
        var visit = MutableList(tickets.size) {false}

        var sortedTickets = tickets.toMutableList().sortedBy{it[1]}


        sortedTickets.forEachIndexed { i, ticket ->
            if(ticket[0] == "ICN") {
                visit[i] = true
                dfs(sortedTickets, visit, ticket ,1, mutableListOf(ticket[0], ticket[1]))
                visit[i] = false
            }
        }


        return possibleRoutes[0].toTypedArray()
    }

    fun dfs(tickets: List<Array<String>>, visit: MutableList<Boolean>, currentTicket: Array<String>, count: Int, route: MutableList<String>) {

        if(count == tickets.size) {
            var routeTemp = route.toList()
            possibleRoutes.add(routeTemp)
            return
        }

        for(i in 0 until tickets.size) {

            if(visit[i] == true || currentTicket[1] != tickets[i][0]) continue


            visit[i] = true
            route.add(tickets[i][1])
            dfs(tickets, visit, tickets[i], count+1, route)

            visit[i] = false
            route.removeAt(route.lastIndex)


        }


    }

}