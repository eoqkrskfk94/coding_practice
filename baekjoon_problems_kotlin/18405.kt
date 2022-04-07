import java.util.LinkedList


fun main() {

    val br = System.`in`.bufferedReader()

    val (n, k) = br.readLine().split(" ").map { it.toInt() }

    var map = mutableListOf<MutableList<Int>>()

    repeat(n) {
        map.add(br.readLine().split(" ").map { it.toInt() }.toMutableList())
    }

    val (s, x, y) = br.readLine().split(" ").map { it.toInt() }

    bfs(map, n, k, s, x, y)


}

fun bfs(map: MutableList<MutableList<Int>>, n: Int, k: Int, s: Int, x: Int, y: Int) {

    val queue = LinkedList<List<Int>>()
    var initialVirusPoints = mutableListOf<List<Int>>()

    val dx = listOf(0,0,-1,1)
    val dy = listOf(-1,1,0,0)

    for (i in 0 until n) {
        for (j in 0 until n) {
            if (map[i][j] > 0) {
                queue.add(listOf(map[i][j], i, j))
            }
        }
    }

//    initialVirusPoints.sortedBy { it[0] }.forEach {
//        queue.add(it)
//    }


    for (i in 1..s) {

        queue.sortBy { it[0] }
        var queueSize = queue.size

        for (j in 0 until queueSize) {
            val (virusNum, x, y) = queue.poll()

            for(k in 0 .. 3) {
                val nx = x + dx[k]
                val ny = y + dy[k]

                if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue

                if(map[nx][ny] == 0) {
                    map[nx][ny] = map[x][y]
                    queue.add(listOf(map[nx][ny], nx, ny))
                }
            }
        }

//        for (j in map.indices) {
//            println(map[j])
//        }


    }


    println(map[x-1][y-1])
}


