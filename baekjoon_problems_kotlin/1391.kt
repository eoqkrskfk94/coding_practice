data class Meeting(val start: Int, var end: Int)

fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    var numOfMeetings = br.readLine().toInt()
    var meetings = mutableListOf<Meeting>()
    var totalCount = 0
    var endTime = 0


    repeat(numOfMeetings) {
        val (start: Int, end: Int) = br.readLine().split(" ").map { it.toInt() }
        meetings.add(Meeting(start, end))
    }

    meetings = meetings.sortedWith(compareBy { it.start }).toMutableList()
    meetings = meetings.sortedWith(compareBy { it.end }).toMutableList()



    meetings.forEach {
        if(it.end >= endTime && it.start >= endTime) {
            endTime = it.end
            totalCount++
        }
    }


    println(totalCount)

}