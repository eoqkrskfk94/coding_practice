import java.util.LinkedList

var blocks = mutableSetOf<List<Pair<Int, Int>>>()
var answer = 0

fun main() {

    val br = System.`in`.bufferedReader()

    val (n, m) = br.readLine().split(" ").map { it.toInt() }

    var graph = mutableListOf<MutableList<Int>>()
    var virus = mutableListOf<Pair<Int, Int>>()
    var floors = mutableListOf<Pair<Int, Int>>()

    repeat(n) {
        graph.add(br.readLine().split(" ").map { it.toInt() }.toMutableList())
    }

    for (i in 0 until graph.size) {
        for (j in 0 until graph[i].size) {
            if(graph[i][j] == 0) floors.add(Pair(i,j))
            else if(graph[i][j] == 2) virus.add(Pair(i,j))
        }
    }

    combinations(floors, MutableList(floors.size) {false}, 0, mutableListOf())

    var blocksList = blocks.toList()
    for(i in 0 until blocksList.size) {
        bfs(n, m, graph, blocksList[i], virus)
    }


    println(answer)
}

fun combinations(floors: MutableList<Pair<Int, Int>>, visit: MutableList<Boolean> , count: Int, comb: MutableList<Pair<Int,Int>>) {

    if(count == 3) {
        blocks.add(comb.sortedBy { it.first }.sortedBy { it.second })
        return
    }

    for(i in 0 until floors.size) {
        if(visit[i] == true) continue

        visit[i] = true
        comb.add(floors[i])
        combinations(floors, visit, count+1, comb)

        visit[i] = false
        comb.removeAt(comb.lastIndex)

    }


}


fun bfs(n: Int, m: Int, graph: MutableList<MutableList<Int>>, block: List<Pair<Int, Int>>, virus: MutableList<Pair<Int, Int>>) {

    var newGraph = graph.map { it.toMutableList() }


    block.forEach {
        newGraph[it.first][it.second] = 1
    }

//    for (i in 0 until newGraph.size) {
//        println(newGraph[i])
//    }

    var queue = LinkedList<Pair<Int, Int>>()

    virus.forEach {
        queue.add(it)
    }

    val dx = listOf(0,0,-1,1)
    val dy = listOf(-1,1,0,0)

    while (queue.isNotEmpty()) {

        var (x, y) = queue.poll()

        for (i in 0 until 4) {
            var nx = x + dx[i]
            var ny = y + dy[i]

            if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue

            if(newGraph[nx][ny] == 0) {
                newGraph[nx][ny] = 2
                queue.add(Pair(nx, ny))
            }
        }
    }


    var saveZoneCount = 0

    for (i in 0 until n) {
        for (j in 0 until m) {
            if(newGraph[i][j] == 0) saveZoneCount++
        }
    }

    if(answer < saveZoneCount) answer = saveZoneCount
}

