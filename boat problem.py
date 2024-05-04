#You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a
# maximum weight of limit.
# Each boat carries at most two people at the same time,
#provided the sum of the weight of those people is at most limit.

people = [233,23,56,7,8,7]
limit =300
def numRescueBoats(self, people: list[int], limit: int) -> int:
  """
  This function calculates the minimum number of boats needed to transport all people.

  Args:
      people: List[int] - List containing weights of each person.
      limit: int - Maximum weight capacity of a boat.

  Returns:
      int - Minimum number of boats required.
  """

  # Sort the people list in ascending order (lightest to heaviest)
  people.sort()

  # Initialize two pointers: i (lightest) and j (heaviest)
  i = 0
  j = len(people) - 1
  boats = 0

  # Loop until both pointers meet
  while i <= j:
    # If lightest and heaviest can fit in one boat, use it
    if people[i] + people[j] <= limit:
      i += 1  # Move lightest pointer to next person
    else:
      j -= 1  # Move heaviest pointer to previous person (avoid exceeding limit)
    boats += 1  # Increment boat count after each successful pairing or single placement

  return boats

boats_needed = numRescueBoats(None, people, limit)  # Since self is not used
print(f"Minimum number of boats needed: {boats_needed}")