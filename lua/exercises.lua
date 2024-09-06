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
    -- concatenation helper function 
    local function combine(word)
      -- instead of for loop, return the function to itself so that itll run again  
      if word then
            table.insert(words, word)
            return combine 
        else
            return table.concat(words, " ")
        end
    end

    -- start the chain of words
    if sentence then
        table.insert(words, sentence)
        return combine
    else
        return ""
    end
end

-- Write your line count function here
-- open file, if file can't be open throw an error, if it can be openned iterate over each line in the file, get rid of whitespace, if not empty add it
  function meaningful_line_count(file)
      -- Attempt to open the file for reading
      local f, err = io.open(file, "r")
      local counter = 0
      if not f then
          error("Can't open file: " .. err)
      end
      for line in f:lines() do
        --whitespace strip
          line = line:match("^%s*(.-)%s*$")
          if line ~= "" and not line:find("^#") then
              counter = counter + 1
          end
      end
      f:close()
      return counter
  end

-- Write your Quaternion table here
