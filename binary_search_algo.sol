// SPDX-License-Identifier: MIT
// Created by: Siyi Xu (All rights reserved)
pragma solidity ^0.8.0;
// Binary search algorithm using solidity(written in smart contract form)

contract BinarySearch {

    // Function to perform binary search on a sorted array
    function binarySearch(uint[] memory array, uint target) public pure returns (int) {
        int left = 0;
        int right = int(array.length) - 1;

        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (array[uint(middle)] == target) {
                return middle;
            }
            if (array[uint(middle)] < target) {
                left = middle + 1;
            }
            
            else {
                right = middle - 1;
            }
        }

        // Target was not found in the array
        return -1;
    }
}
