module.exports = (robot) ->
  robot.hear /check gender for (.*)/i, (res) ->
    personName = escape(res.match[1])
    res.http("https://api.genderize.io/?name=" + personName)
      .get() (error, response, body) ->
      try
        json = JSON.parse(body)
        res.send "Probability of " + "#{json.probability}" + " that " + personName + " is a " + "#{json.gender}.\n"
      catch error
        res.send "something went wrong..."