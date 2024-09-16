import React, { SVGProps } from 'react';

const SvgWaterMixer = (props: SVGProps<SVGSVGElement>) => {
	return (
		<svg viewBox='0 0 24 24' className='svg-icon' {...props}>
			<g fill='none' fillRule='evenodd'>
				<path d='M0 0h24v24H0z' />
				<path d='M8 18a4 4 0 014 4H4a4 4 0 014-4z' fill='currentColor' opacity={0.3} />
				<path
					d='M7 12.126V8a6 6 0 1112 0v1h-2V8a4 4 0 10-8 0v4.126A4.002 4.002 0 018 20a4 4 0 01-1-7.874zM8 18a2 2 0 100-4 2 2 0 000 4z'
					fill='currentColor'
				/>
				<path
					d='M18 17a2 2 0 002-2c0-.736-.667-1.736-2-3-1.333 1.264-2 2.264-2 3a2 2 0 002 2z'
					fill='currentColor'
					opacity={0.3}
				/>
			</g>
		</svg>
	);
};

export default SvgWaterMixer;
