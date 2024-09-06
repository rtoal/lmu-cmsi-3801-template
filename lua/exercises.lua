function change(amount)
  if math.type(amount) ~= "integer" then
    error("Amount must be an integer")
  end
  if amount < 0 then
    error("Amount cannot be negative")
  end
  local counts, remaining = {}, amount
  for _, denomination in ipairs({25, 10, 5, 1}) do
    counts[denomination] = remaining // denomination
    remaining = remaining % denomination
  end
  return counts
end

-- Write your first then lower case function here
function first_then_lower_case(strings, predicate)
  for idx = 0, #strings do
    if strings[idx] ~= nil and predicate(strings[idx]) then
      return string.lower(strings[idx])
    end
  end
  return nil
end

-- Write your powers generator here

-- Write your say function here

-- Write your line count function here
function meaningful_line_count(path)
  file = io.open(path)
  count = 0
  for line in file:lines() do 
    line = line:gsub("%s+", "")
    if not line.len == 0 or not line[1] == "#" then
      count += 1
    end
  end
  file.close()
  return count
end 

-- Write your Quaternion table here
