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
  function first_then_lower_case(a, p)
    for _, i in ipairs(a) do
      if p(i) then
        return string.lower(i)        
      end
    end
    return nil
  end

-- Write your powers generator here
function powers_generator(base, limit)
  local total = 1
  -- create coroutine
  return coroutine.create(function()
    while total <= limit do
      -- pause coroutine and return total
      coroutine.yield(total)
      total = total * base
    end
  -- need to close coroutine with parenthesis
  end)
end

-- Write your say function here
  function say(sentence)
    local words = {}
    if sentence then
      table.insert(words, sentence)
    end
    local output

    for 

  end

-- Write your line count function here
  --function meaningful_line_count(file)

-- Write your Quaternion table here
