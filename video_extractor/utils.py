import re


def parse_subtitles(subtitles_text):
    """
    Parses the subtitles text from an SRT file and returns a list of dictionaries
    with keys 'text', 'start_time', and 'end_time'.
    """
    subtitles = []
    blocks = subtitles_text.strip().split("\n\n")

    for block in blocks:
        lines = block.split("\n")

        if len(lines) < 3:
            continue

        text = "\n".join(lines[2:])
        text = re.sub(r"<[^>]+>", "", text)  # Remove any HTML tags like <font>

        timing = lines[1]

        match = re.match(
            r"(\d{2}):(\d{2}):(\d{2}),(\d{3}) --> (\d{2}):(\d{2}):(\d{2}),(\d{3})",
            timing,
        )
        if match:
            start_time = (
                int(match.group(1)) * 3600
                + int(match.group(2)) * 60
                + int(match.group(3))
                + int(match.group(4)) / 1000
            )
            end_time = (
                int(match.group(5)) * 3600
                + int(match.group(6)) * 60
                + int(match.group(7))
                + int(match.group(8)) / 1000
            )
            subtitles.append(
                {"text": text.strip(), "start_time": start_time, "end_time": end_time}
            )

    return subtitles
