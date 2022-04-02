class Solution {
    fun solution(id_list: Array<String>, report: Array<String>, k: Int): IntArray {
        var answer = MutableList(id_list.size) {0}
        var reportMap = mutableMapOf<String, MutableSet<String>>()
        var reportCounts = mutableMapOf<String, Int>()
        var stopedUsers = mutableSetOf<String>()

        report.forEach {
            var reportNames = it.split(" ")
            if(!reportMap.contains(reportNames[0])) {
                reportMap[reportNames[0]] = mutableSetOf(reportNames[1])
            } else {
                reportMap[reportNames[0]]!!.add(reportNames[1])
            }
        }

        id_list.forEach {id ->
            var reportList = reportMap[id]?.toList() ?: listOf()

            reportList.forEach {
                if(!reportCounts.contains(it)) {
                    reportCounts[it] = 1
                } else {
                    reportCounts[it] = reportCounts[it]!!.plus(1)
                }

                if(reportCounts[it]!! >= k) {
                    stopedUsers.add(it)
                }
            }
        }

        id_list.forEachIndexed { index , user ->

            stopedUsers.toList().forEach {
                if(reportMap[user]?.contains(it) ?: false) {
                    answer[index]++
                }
            }
        }



        // println(reportMap)
        // println(reportCounts)
        // println(stopedUsers)




        return answer.toIntArray()
    }
}