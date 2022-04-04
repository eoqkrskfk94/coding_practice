class Solution {
    lateinit var INFO: IntArray
    lateinit var list: Array<ArrayList<Int>>
    lateinit var visit: MutableList<Boolean>
    var answer = 0

    fun solution(info: IntArray, edges: Array<IntArray>): Int {
        INFO = info
        list = Array(info.size) { ArrayList<Int>()}
        visit = MutableList(info.size) {false}

        for (edge in edges) {
            val start = edge[0]
            val end = edge[1]
            list[start].add(end)
        }

        dfs(mutableListOf() ,0,0,0, mutableListOf(0))

        return answer
    }

    fun dfs(possibleRoutes: MutableList<Int>, sheeps: Int, wolves: Int, current: Int, route: MutableList<Int>) {

        var curSheeps = sheeps
        var curWolves = wolves

        when(INFO[current]) {
            0 -> curSheeps++
            1 -> curWolves++
        }

        if(curWolves >= curSheeps) {
            return
        }

        if(answer < curSheeps) answer = curSheeps


        for(i in list[current]) {
            possibleRoutes.add(i)
        }


        for(num in possibleRoutes) {
            if(visit[num] == true) continue

            route.add(num)
            visit[num] = true

            dfs(possibleRoutes.toMutableList(), curSheeps, curWolves, num, route)

            route.removeAt(route.lastIndex)
            visit[num] = false
        }


    }

}