class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Initial thoughts
        # 
        # Last value will always be -1
        # Second last value will always be arr[-1]

        # Last value being -1 hints at an elegant solution
        # End loop on last and hard code -1 for now

        # Currently making a copy of array at every pass
        # Instead, remove arr[0] at each go, get max of arr[i + 1:]

        i = 0
        while i < len(arr) - 1:
            arr[i] = max(arr[i + 1:])

            i += 1

        arr[-1] = -1

        return arr