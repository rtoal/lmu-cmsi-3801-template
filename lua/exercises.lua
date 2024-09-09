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
function powers_generator(base, limit)
  return coroutine.create(function()
    local power = 1
    while power <= limit do
      coroutine.yield(power)
      power = power * base  
    end
  end)
end

-- Write your say function here
function say(text)
  --[[
  Say function concatenates string functions and chains together to create one final string phrase
  ]]--
  sentence = {}

  function final_sentence(next_text)
    if next_text == nil then 
      return table.concat(sentence, " ")
    else
      table.insert(sentence, next_text)
    end
    return final_sentence
  end 
  if text == nil then 
    return ""
  end 

  table.insert(sentence, text)
  return final_sentence
end

-- Write your line count function here
function meaningful_line_count(filepath)
  linecount = 0
  file = io.open(filepath, "r")

  if file == nil then 
    error("No such file")
  end
  
  for line in file:lines() do
    line = line:match("^%s*(.-)%s*$")

    if (line ~= "" and not line:match("^#")) then
        linecount = linecount + 1
    end
  end

  file:close()    
  return linecount
end

-- Write your Quaternion table here
