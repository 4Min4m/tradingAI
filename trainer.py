class AgentTrainer:
    def __init__(self, model, optimizer, loss_fn):
        self.model = model
        self.optimizer = optimizer
        self.loss_fn = loss_fn

    def train(self, data, labels, epochs=10):
        for epoch in range(epochs):
            self.optimizer.zero_grad()
            predictions = self.model(data)
            loss = self.loss_fn(predictions, labels)
            loss.backward()
            self.optimizer.step()
            print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item()}")