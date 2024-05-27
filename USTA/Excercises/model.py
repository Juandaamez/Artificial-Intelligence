from pomegranate import Node, DicreteDistribution, ConditionalProbabilityTable

rain = Node(DiscreteDistribution({
    "none": 0.7,
    "light": 0.2,
    "heavy": 0.1,
}),
            name="rain")

maintenance = Node(
    ConditionalProbabilityTable({
        ["none", "yes", 0.4],
        ["none", "no", 0.6],
        ["light", "yes", 0.2],
        ["light", "no", 0.8],
        ["heavy", "yes", 0.1],
        ["heavy", "no", 0.9],
    })
    name = "maintenance"
)

train = Node(
    ConditionalProbabilityTable(
        [
            ["none", "yes", "on time", 0.8],
            ["none", "yes", "delayed", 0.8],
            ["none", "no", "on time", 0.8],
            ["none", "no", "delayed", 0.8],
            ["light", "yes", "on time", 0.8],
            ["light", "yes", "delayed", 0.8],
            ["light", "no", "on time", 0.8],
            ["light", "no", "delayed", 0.8],
            ["heavy", "yes", "on time", 0.8],
            ["heavy", "yes", "delayed", 0.8],
            ["heavy", "no", "on time", 0.8],
            ["heavy", "no", "delayed", 0.8],
        ],
        [rain.distribution, maintenance.distribution]
    )
    name = "train"
)

appointment = Node(
    ConditionalProbabilityTable(
        [
            ["on time", "attend", 0.9],
            ["on time", "miss", 0.9],
            ["delayed", "attend", 0.9],
            ["delayed", "miss", 0.9],
        ]
    )
)
