var networkCount = 0
var computerNetwork = arrayListOf<IntArray>()

class Solution {
    fun solution(n: Int, computers: Array<IntArray>): Int {

        var sets = mutableSetOf<List<Int>>()
        computerNetwork = computers.toCollection(ArrayList())


        for(i in 0 until n) {
            val route = dfs(i, n, arrayListOf<Int>(), MutableList(n){false})
            sets.add(route.sorted())
        }

        println(sets)
        return sets.size
    }

    fun dfs(startNode: Int, n: Int, comb: ArrayList<Int>, visit: MutableList<Boolean>): ArrayList<Int> {

        visit[startNode] = true
        comb.add(startNode)

        for(i in 0 until n) {
            if(visit[i] == true || computerNetwork[startNode][i] == 0) continue
            dfs(i , n, comb, visit)
        }

        return comb

    }
}