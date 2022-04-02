import kotlin.math.*

class Solution {
    fun solution(fees: IntArray, records: Array<String>): IntArray {
        var answer = mutableListOf<Int>()
        var carRecords = mutableMapOf<String, MutableList<String>>()
        var carNumbers = mutableListOf<String>()

        records.forEach {
            var record = it.split(" ")
            if(!carRecords.contains(record[1])) {
                carRecords[record[1]] = mutableListOf(record[0])
                carNumbers.add(record[1])
            } else {
                carRecords[record[1]]!!.add(record[0])
            }
        }

        carNumbers.sort()


        carNumbers.forEach { carNumber ->

            var carRecord = carRecords[carNumber]!!
            var carIn = true
            var totalTime = 0

            carRecord.forEachIndexed { index, record ->
                if(carIn == true) {
                    carIn = false

                    if(index == carRecord.size - 1) {
                        totalTime += getTotalMinFromTimeString(carRecord[index], "23:59")
                    }

                } else {
                    totalTime += getTotalMinFromTimeString(carRecord[index - 1], carRecord[index])
                    carIn = true
                }
            }
            answer.add(getFee(fees, totalTime))
        }


        return answer.toIntArray()
    }


    fun getFee(fees: IntArray, totalMin: Int): Int {

        if(totalMin <= fees[0]) return fees[1]

        var fee = fees[1] + ((totalMin - fees[0]) / fees[2]) * fees[3]

        if((totalMin - fees[0]) % fees[2] > 0) fee += fees[3]

        return fee
    }

    fun getTotalMinFromTimeString(startTime: String, endTime: String): Int {
        return getMinFromTimeString(endTime) - getMinFromTimeString(startTime)
    }

    fun getMinFromTimeString(time: String): Int {

        var (hour, min) = time.split(":").map{it.toInt()}

        return (hour * 60) + min

    }
}