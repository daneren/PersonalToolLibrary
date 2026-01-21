def calculate_workload(seqlen_list: torch.Tensor) -> torch.Tensor:
    """Calculate approximate computational workload for transformer attention.

    Estimates FLOPs for dense transformer blocks based on sequence length using
    the formula: FLOPs ≈ 12 * hidden_size² * seqlen + 2 * hidden_size * seqlen²

    The constants are calibrated for a 7B model (hidden_size=4096), yielding:
    workload ∝ 24576 * seqlen + seqlen²

    Args:
        seqlen_list: Sequence lengths as a tensor.

    Returns:
        torch.Tensor: Estimated workload values proportional to actual FLOPs.

    Note:
        The returned values are relative workloads, not actual FLOP counts.
        Useful for balancing computation across data parallel ranks.
    """
    return 24576 * seqlen_list + seqlen_list**2
